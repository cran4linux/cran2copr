%global packname  agrmt
%global packver   1.40.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.40.4
Release:          1%{?dist}
Summary:          Calculate Agreement or Consensus in Ordered Rating Scales

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
Calculate agreement or consensus in ordered rating scales. The package
implements van der Eijk's (2001) <DOI: 10.1023/A:1010374114305> measure of
agreement A, which can be used to describe agreement, consensus, or
polarization among respondents. It also implements measures of consensus
(dispersion) by Leik, Tatsle and Wierman, Blair and Lacy, Kvalseth, Berry
and Mielke, and Garcia-Montalvo and Reynal-Querol. Furthermore, an
implementation of Galtungs AJUS-system is provided to classify
distributions, as well as a function to identify the position of multiple
modes.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
