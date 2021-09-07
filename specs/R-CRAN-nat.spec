%global __brp_check_rpaths %{nil}
%global packname  nat
%global packver   1.8.18
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.8.18
Release:          1%{?dist}%{?buildtag}
Summary:          NeuroAnatomy Toolbox for Analysis of 3D Image Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.15.1
Requires:         R-core >= 2.15.1
BuildArch:        noarch
BuildRequires:    R-CRAN-filehash >= 2.3
BuildRequires:    R-CRAN-rgl >= 0.98.1
BuildRequires:    R-CRAN-igraph >= 0.7.1
BuildRequires:    R-CRAN-nat.utils >= 0.4.2
BuildRequires:    R-CRAN-nabor 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-yaml 
Requires:         R-CRAN-filehash >= 2.3
Requires:         R-CRAN-rgl >= 0.98.1
Requires:         R-CRAN-igraph >= 0.7.1
Requires:         R-CRAN-nat.utils >= 0.4.2
Requires:         R-CRAN-nabor 
Requires:         R-methods 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-yaml 

%description
NeuroAnatomy Toolbox (nat) enables analysis and visualisation of 3D
biological image data, especially traced neurons. Reads and writes 3D
images in NRRD and 'Amira' AmiraMesh formats and reads surfaces in 'Amira'
hxsurf format. Traced neurons can be imported from and written to SWC and
'Amira' LineSet and SkeletonGraph formats. These data can then be
visualised in 3D via 'rgl', manipulated including applying calculated
registrations, e.g. using the 'CMTK' registration suite, and analysed.
There is also a simple representation for neurons that have been subjected
to 3D skeletonisation but not formally traced; this allows morphological
comparison between neurons including searches and clustering (via the
'nat.nblast' extension package).

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
