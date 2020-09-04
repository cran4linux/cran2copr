%global packname  phenopix
%global packver   2.4.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.4.2
Release:          1%{?dist}%{?buildtag}
Summary:          Process Digital Images of a Vegetation Cover

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.15.3
Requires:         R-core >= 2.15.3
BuildArch:        noarch
BuildRequires:    R-CRAN-stringr >= 1.0.0
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-jpeg 
BuildRequires:    R-CRAN-bcp 
BuildRequires:    R-CRAN-strucchange 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-iterators 
BuildRequires:    R-CRAN-gtools 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-sp 
Requires:         R-CRAN-stringr >= 1.0.0
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-jpeg 
Requires:         R-CRAN-bcp 
Requires:         R-CRAN-strucchange 
Requires:         R-parallel 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-iterators 
Requires:         R-CRAN-gtools 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-sp 

%description
A collection of functions to process digital images, depict greenness
index trajectories and extract relevant phenological stages.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
