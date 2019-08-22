%global packname  BeyondBenford
%global packver   1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1
Release:          1%{?dist}
Summary:          Compare the Goodness of Fit of Benford's and Blondeau Da Silva'sDigit Distributions to a Given Dataset

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
Allows to compare the goodness of fit of Benford's and Blondeau Da Silva's
digit distributions in a dataset. It is used to check whether the data
distribution is consistent with theoretical distributions highlighted by
Blondeau Da Silva or not (through the dat.distr() function): this ideal
theoretical distribution must be at least approximately followed by the
data for the use of Blondeau Da Silva's model to be well-founded. It also
enables to plot histograms of digit distributions, both observed in the
dataset and given by the two theoretical approaches (with the digit.ditr()
function). Finally, it proposes to quantify the goodness of fit via
Pearson's chi-squared test (with the chi2() function).

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
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
