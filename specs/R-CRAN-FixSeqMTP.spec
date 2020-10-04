%global packname  FixSeqMTP
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          3%{?dist}%{?buildtag}
Summary:          Fixed Sequence Multiple Testing Procedures

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
Several generalized / directional Fixed Sequence Multiple Testing
Procedures (FSMTPs) are developed for testing a sequence of pre-ordered
hypotheses while controlling the FWER, FDR and Directional Error (mdFWER).
All three FWER controlling generalized FSMTPs are designed under arbitrary
dependence, which allow any number of acceptances. Two FDR controlling
generalized FSMTPs are respectively designed under arbitrary dependence
and independence, which allow more but a given number of acceptances. Two
mdFWER controlling directional FSMTPs are respectively designed under
arbitrary dependence and independence, which can also make directional
decisions based on the signs of the test statistics. The main functions
for each proposed generalized / directional FSMTPs are designed to
calculate adjusted p-values and critical values, respectively. For users'
convenience, the functions also provide the output option for printing
decision rules.

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
