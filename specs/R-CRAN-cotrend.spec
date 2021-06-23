%global __brp_check_rpaths %{nil}
%global packname  cotrend
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          3%{?dist}%{?buildtag}
Summary:          Consistent Co-Trending Rank Selection

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-xts 
Requires:         R-CRAN-xts 

%description
Implements cointegration/co-trending rank selection algorithm in Guo and
Shintani (2013) "Consistent co-trending rank selection when both
stochastic and nonlinear deterministic trends are present". The
Econometrics Journal 16: 473-483 <doi:10.1111/j.1368-423X.2012.00392.x>.
Numbered examples correspond to Feb 2011 preprint
<http://www.fas.nus.edu.sg/ecs/events/seminar/seminar-papers/05Apr11.pdf>.

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
