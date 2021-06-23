%global __brp_check_rpaths %{nil}
%global packname  MDBED
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          2%{?dist}%{?buildtag}
Summary:          Moran-Downton Bivariate Exponential Distribution

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-CRAN-orthopolynom 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-lattice 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-psych 
BuildRequires:    R-stats 
Requires:         R-CRAN-Rdpack 
Requires:         R-CRAN-orthopolynom 
Requires:         R-CRAN-foreach 
Requires:         R-lattice 
Requires:         R-parallel 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-ggplot2 
Requires:         R-graphics 
Requires:         R-CRAN-psych 
Requires:         R-stats 

%description
Provides 3D plots of the Moran-Downton bivariate exponential distribution
(MDBED), generates bivariate random values, and also provides values of
the joint and conditional PDFs and CDFs. Nagao M, Kadoya M (1971)
<http://hdl.handle.net/2433/124795>. Balakrishna N, Lai CD (2009)
<doi:10.1007/b101765>.

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

%files
%{rlibdir}/%{packname}
