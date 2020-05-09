%global packname  catseyes
%global packver   0.2.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.5
Release:          1%{?dist}
Summary:          Create Catseye Plots Illustrating the Normal Distribution of theMeans

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
Provides the tools to produce catseye plots, principally by catseyesplot()
function which calls R's standard plot() function internally, or
alternatively by the catseyes() function to overlay the catseye plot onto
an existing R plot window. Catseye plots illustrate the normal
distribution of the mean (picture a normal bell curve reflected over its
base and rotated 90 degrees), with a shaded confidence interval; they are
an intuitive way of illustrating and comparing normally distributed
estimates, and are arguably a superior alternative to standard confidence
intervals, since they show the full distribution rather than fixed
quantile bounds. The catseyesplot and catseyes functions require
pre-calculated means and standard errors (or standard deviations),
provided as numeric vectors; this allows the flexibility of obtaining this
information from a variety of sources, such as direct calculation or
prediction from a model.  Catseye plots, as illustrations of the normal
distribution of the means, are described in Cumming (2013 & 2014).
Cumming, G. (2013). The new statistics: Why and how. Psychological
Science, 27, 7-29. <doi:10.1177/0956797613504966> pmid:24220629.

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
