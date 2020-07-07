%global packname  IrregLong
%global packver   0.3.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.2
Release:          2%{?dist}
Summary:          Analysis of Longitudinal Data with Irregular Observation Times

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-survival 
BuildRequires:    R-CRAN-geepack 
BuildRequires:    R-CRAN-frailtypack 
BuildRequires:    R-CRAN-data.table 
Requires:         R-survival 
Requires:         R-CRAN-geepack 
Requires:         R-CRAN-frailtypack 
Requires:         R-CRAN-data.table 

%description
Analysis of longitudinal data for which the times of observation are
random variables that are potentially associated with the outcome process.
The package includes inverse-intensity weighting methods (Lin H,
Scharfstein DO, Rosenheck RA (2004)
<doi:10.1111/j.1467-9868.2004.b5543.x>) and multiple outputation
(Pullenayegum EM (2016) <doi:10.1002/sim.6829>).

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
