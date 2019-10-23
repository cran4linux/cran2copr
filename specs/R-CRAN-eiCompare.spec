%global packname  eiCompare
%global packver   2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1
Release:          1%{?dist}
Summary:          Compares EI, Goodman, RxC Estimates

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-eiPack 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-tmvtnorm 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ei 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-ucminf 
BuildRequires:    R-CRAN-R.utils 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-msm 
BuildRequires:    R-CRAN-mnormt 
BuildRequires:    R-CRAN-cubature 
BuildRequires:    R-CRAN-ellipse 
BuildRequires:    R-CRAN-plotrix 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-stringr 
Requires:         R-CRAN-eiPack 
Requires:         R-methods 
Requires:         R-CRAN-tmvtnorm 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ei 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-ucminf 
Requires:         R-CRAN-R.utils 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-msm 
Requires:         R-CRAN-mnormt 
Requires:         R-CRAN-cubature 
Requires:         R-CRAN-ellipse 
Requires:         R-CRAN-plotrix 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-stringr 

%description
Compares estimates from three ecological inference routines, based on King
(1997) <ISBN: 0691012407>,
<http://gking.harvard.edu/eicamera/kinroot.html>; King et. al. (2004)
<ISBN: 0521542804>,
<http://gking.harvard.edu/files/abs/ecinf04-abs.shtml>.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/data
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
