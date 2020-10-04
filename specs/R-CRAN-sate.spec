%global packname  sate
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          3%{?dist}%{?buildtag}
Summary:          Scientific Analysis of Trial Errors (SATE)

License:          CC0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0
Requires:         R-core >= 3.0
BuildArch:        noarch
BuildRequires:    R-MASS 
BuildRequires:    R-stats 
Requires:         R-MASS 
Requires:         R-stats 

%description
Bundles functions used to analyze the harmfulness of trial errors in
criminal trials. Functions in the Scientific Analysis of Trial Errors
('SATE') package help users estimate the probability that a jury will find
a defendant guilty given jurors' preferences for a guilty verdict and the
uncertainty of that estimate. Users can also compare actual and
hypothetical trial conditions to conduct harmful error analysis. The
relationship between individual jurors' verdict preferences and the
probability that a jury returns a guilty verdict has been studied by Davis
(1973) <doi:10.1037/h0033951>; MacCoun & Kerr (1988)
<doi:10.1037/0022-3514.54.1.21>, and Devine et el. (2001)
<doi:10.1037/1076-8971.7.3.622>, among others.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
