%global packname  TEQR
%global packver   6.0-0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          6.0.0
Release:          2%{?dist}
Summary:          Target Equivalence Range Design

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
The TEQR package contains software to calculate the operating
characteristics for the TEQR and the ACT designs.The TEQR (toxicity
equivalence range) design is a toxicity based cumulative cohort design
with added safety rules. The ACT (Activity constrained for toxicity)
design is also a cumulative cohort design with additional safety rules.
The unique feature of this design is that dose is escalated based on lack
of activity rather than on lack of toxicity and is de-escalated only if an
unacceptable level of toxicity is experienced.

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
