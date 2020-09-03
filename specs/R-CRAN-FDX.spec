%global packname  FDX
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          False Discovery Exceedance Controlling Multiple Testing Procedures

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.00
Requires:         R-core >= 3.00
BuildRequires:    R-CRAN-PoissonBinomial >= 1.1.2
BuildRequires:    R-CRAN-Rcpp >= 1.0.3
BuildRequires:    R-CRAN-DiscreteFDR 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-pracma 
Requires:         R-CRAN-PoissonBinomial >= 1.1.2
Requires:         R-CRAN-Rcpp >= 1.0.3
Requires:         R-CRAN-DiscreteFDR 
Requires:         R-methods 
Requires:         R-CRAN-pracma 

%description
Multiple testing procedures for heterogeneous and discrete tests as
described in Döhler and Roquain (2019) <arXiv:1912.04607v1>. The main
algorithms of the paper are available as continuous, discrete and weighted
versions.

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
