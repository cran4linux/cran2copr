%global packname  SPAtest
%global packver   3.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.0.2
Release:          1%{?dist}
Summary:          Score Test and Meta-Analysis Based on Saddlepoint Approximation

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch

%description
Performs score test using saddlepoint approximation to estimate the null
distribution. Also prepares summary statistics for meta-analysis and
performs meta-analysis to combine multiple association results. For the
latest version, please check <https://github.com/leeshawn/SPAtest>.

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
