%global packname  WWR
%global packver   1.2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.2
Release:          3%{?dist}%{?buildtag}
Summary:          Weighted Win Loss Statistics and their Variances

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.2
Requires:         R-core >= 3.1.2
BuildRequires:    R-CRAN-inline 
BuildRequires:    R-stats 
Requires:         R-CRAN-inline 
Requires:         R-stats 

%description
Calculate the (weighted) win loss statistics including the win ratio, win
difference and win product and their variances, with which the p-values
are also calculated. The variance estimation is based on Luo et al. (2015)
<doi:10.1111/biom.12225> and Luo et al. (2017) <doi:10.1002/sim.7284>.
This package also calculates general win loss statistics with
user-specified win loss function with variance estimation based on Bebu
and Lachin (2016) <doi:10.1093/biostatistics/kxv032>. This version
corrected an error when outputting confidence interval for win difference.

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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
