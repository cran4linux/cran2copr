%global packname  raincin
%global packver   1.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.3
Release:          1%{?dist}
Summary:          Ranking with Incomplete Information

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-CRAN-popdemo 
BuildRequires:    R-stats 
Requires:         R-CRAN-lme4 
Requires:         R-CRAN-popdemo 
Requires:         R-stats 

%description
Various statistical and mathematical ranking and rating methods with
incomplete information are included. This package is initially designed
for the scoring system in a high school project showcase to rank student
research projects, where each judge can only evaluate a set of projects in
a limited time period. See Langville, A. N. and Meyer, C. D. (2012), Who
is Number 1: The Science of Rating and Ranking, Princeton University Press
<doi:10.1515/9781400841677>, and Gou, J. and Wu, S. (2020), A Judging
System for Project Showcase: Rating and Ranking with Incomplete
Information, Technical Report.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

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
