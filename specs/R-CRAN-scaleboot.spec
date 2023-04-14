%global __brp_check_rpaths %{nil}
%global packname  scaleboot
%global packver   1.0-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          3%{?dist}%{?buildtag}
Summary:          Approximately Unbiased P-Values via Multiscale Bootstrap

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-pvclust >= 2.2.0
BuildRequires:    R-CRAN-mvtnorm 
Requires:         R-CRAN-pvclust >= 2.2.0
Requires:         R-CRAN-mvtnorm 

%description
Calculating approximately unbiased (AU) p-values from multiscale bootstrap
probabilities. See Shimodaira (2004) <doi:10.1214/009053604000000823>,
Shimodaira (2008) <doi:10.1016/j.jspi.2007.04.001>, Terada ans Shimodaira
(2017) <arXiv:1711.00949>, and Shimodaira and Terada (2019)
<doi.org/10.3389/fevo.2019.00174>.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
