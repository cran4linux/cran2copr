%global packname  PubBias
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          3%{?dist}
Summary:          Performs simulation study to look for publication bias, using atechnique described by Ioannidis and Trikalinos; Clin Trials.2007;4(3):245-53.

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-rmeta 
BuildRequires:    R-CRAN-R.utils 
Requires:         R-CRAN-rmeta 
Requires:         R-CRAN-R.utils 

%description
I adapted a method designed by Ioannidis and Trikalinos, which compares
the observed number of positive studies in a meta-analysis with the
expected number, if the summary measure of effect, averaged over the
individual studies, were assumed true. Excess in the observed number of
positive studies, compared to the expected, is taken as evidence of
publication bias. The observed number of positive studies, at a given
level for statistical significance, is calculated by applying Fisher's
exact test to the reported 2x2 table data of each constituent study,
doubling the Fisher one-sided P-value to make a two-sided test. The
corresponding expected number of positive studies was obtained by summing
the statistical powers of each study. The statistical power depended on a
given measure of effect which, here, was the pooled odds ratio of the
meta-analysis was used. By simulating each constituent study, with the
given odds ratio, and the same number of treated and non-treated as in the
real study, the power of the study is estimated as the proportion of
simulated studies that are positive, again by a Fisher's exact test. The
simulated number of events in the treated and untreated groups was done
with binomial sampling. In the untreated group, the binomial proportion
was the percentage of actual events reported in the study and, in the
treated group, the binomial sampling proportion was the untreated
percentage multiplied by the risk ratio which was derived from the assumed
common odds ratio. The statistical significance for judging a positive
study may be varied and large differences between expected and observed
number of positive studies around the level of 0.05 significance
constitutes evidence of publication bias. The difference between the
observed and expected is tested by chi-square. A chi-square test P-value
for the difference below 0.05 is suggestive of publication bias, however,
a less stringent level of 0.1 is often used in studies of publication bias
as the number of published studies is usually small.

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
