%global __brp_check_rpaths %{nil}
%global packname  dief
%global packver   1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2
Release:          3%{?dist}%{?buildtag}
Summary:          Metrics for Continuous Efficiency

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-flux 
BuildRequires:    R-CRAN-fmsb 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-graphics 
BuildRequires:    R-utils 
Requires:         R-CRAN-flux 
Requires:         R-CRAN-fmsb 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-plyr 
Requires:         R-graphics 
Requires:         R-utils 

%description
An implementation of the metrics dief@t and dief@k to measure the
diefficiency (or continuous efficiency) of incremental approaches, see
Acosta, M., Vidal, M. E., & Sure-Vetter, Y. (2017)
<doi:10.1007/978-3-319-68204-4_1>. The metrics dief@t and dief@k allow for
measuring the diefficiency during an elapsed time period t or while k
answers are produced, respectively. dief@t and dief@k rely on the
computation of the area under the curve of answer traces, and thus
capturing the answer rate concentration over a time interval.

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
%{rlibdir}/%{packname}/DESCRIPTION
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
