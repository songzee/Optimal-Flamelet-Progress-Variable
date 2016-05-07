subroutine readdata(YY,ZZ,WW,mzlib,mzprimlib,mxlib,ns)
      implicit none; 
      integer i,j,k,l
      integer,intent(in)::mzlib
      integer,intent(in)::mzprimlib
      integer,intent(in)::mxlib
      integer,intent(in)::ns
      double precision,intent(out),dimension(1:ns,1:mxlib,0:mzlib,1:mzprimlib):: YY
      double precision,intent(out),dimension(0:mzlib):: ZZ
      double precision,intent(out),dimension(1:mxlib,0:mzlib,1:mzprimlib):: WW

       open(100,file='yqavg-lib.txt',action='read') 
        read(100,*) 
           do i=1,mxlib
         read(100,*) 
           do j=0,mzlib
              read(100,*) ZZ(j)
             do k=1,mzprimlib
               read(100,*) 
                read(100,*) (YY(l,i,j,k),l=1,ns)
             enddo
           enddo
	     enddo
	   close(100)


      open(100,file='wavg-lib.txt',action='read') 
        read(100,*) 
           do i=1,mxlib
         read(100,*) 
           do j=0,mzlib
              read(100,*) 
             do k=1,mzprimlib
               read(100,*) 
                read(100,*) WW(i,j,k)
             enddo
           enddo
       enddo
     close(100)
   
 end subroutine readdata


 







!  module mod
!     double precision, intent(out), dimension(:,:,:,:),allocatable :: YY
!     double precision, intent(out), dimension(:),allocatable :: ZZ
!     double precision :: aaa
!     integer :: l,i,j,k,mzlib,mzprimlib,mxlib,ns
 
 
!     ! real,allocatable,dimension(:,:,:),intend(out) :: W
!  contains

! subroutine readdata(YY,ZZ)
 
!     double precision, intent(out), dimension(:,:,:,:),allocatable :: YY
!     double precision, intent(out), dimension(:),allocatable :: ZZ


!    ns=9
!    open(100,file='yqavg-lib.txt',action='read') 
!    read(100,*) mzlib,mzprimlib,mxlib
!    allocate(YY(0:ns-1,0:mxlib-1,0:mzlib,0:mzprimlib-1),ZZ(0:mzlib))
!       do i=0,mxlib-1
!         read(100,*) aaa 
!           do j=0,mzlib
!              read(100,*) ZZ(j)
!             do k=0,mzprimlib-1
!               read(100,*) aaa
!               read(100,*) (YY(l,i,j,k),l=1,ns-1)
!             enddo
!           enddo
! 	    enddo
! 	close(100)
! end subroutine readdata
!   end module mod