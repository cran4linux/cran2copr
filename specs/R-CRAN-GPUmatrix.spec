%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  GPUmatrix
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Basic Linear Algebra with GPU

License:          Artistic-2.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-methods 
Requires:         R-stats 
Requires:         R-methods 

%description
Motivation: GPU power is a great resource for computational biology
specifically in statistics and linear algebra. Unfortunately, very few
packages connect R with the GPU and none of them are transparent enough to
perform the computations on the GPU without substantial changes to the
code. Most of them lack proper maintenance: several of the previous
attempts were removed from the corresponding repositories. It would be
desirable to have an R package, properly maintained, that exploits the use
of the GPU with minimal changes in the existing code. Results: We have
developed the 'GPUMatrix' package. 'GPUMatrix' mimics the behavior of the
Matrix package and extends R to use the GPU for computations. It is easy
to learn and very few changes in the code are required to work on the GPU.
'GPUMatrix' relies on either 'Tensorflow' or 'Torch' R packages to perform
the GPU operations. Its vignette shows some toy examples on non-negative
factorization and other factorization used in 'bioinformatics'.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
[ -d %{packname}/src ] && find %{packname}/src/Make* -type f -exec \
  sed -i 's@-g0@@g' {} \; || true
# don't allow local prefix in executable scripts
find -type f -executable -exec sed -Ei 's@#!( )*/usr/local/bin@#!/usr/bin@g' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
# remove buildroot from installed files
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
