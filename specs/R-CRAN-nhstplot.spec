%global packname  nhstplot
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}
Summary:          Plot Null Hypothesis Significance Tests

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.1
Requires:         R-core >= 3.3.1
BuildArch:        noarch
BuildRequires:    R-stats >= 3.3.1
BuildRequires:    R-grDevices >= 3.3.1
BuildRequires:    R-CRAN-ggplot2 >= 2.2.0
Requires:         R-stats >= 3.3.1
Requires:         R-grDevices >= 3.3.1
Requires:         R-CRAN-ggplot2 >= 2.2.0

%description
Illustrate graphically the most common Null Hypothesis Significance
Testing procedures. More specifically, this package provides functions to
plot Chi-Squared, F, t (one- and two-tailed) and z (one- and two-tailed)
tests, by plotting the probability density under the null hypothesis as a
function of the different test statistic values. Although highly flexible
(color theme, fonts, etc.), only the minimal number of arguments (observed
test statistic, degrees of freedom) are necessary for a clear and useful
graph to be plotted, with the observed test statistic and the p value, as
well as their corresponding value labels. The axes are automatically
scaled to present the relevant part and the overall shape of the
probability density function. This package is especially intended for
education purposes, as it provides a helpful support to help explain the
Null Hypothesis Significance Testing process, its use and/or shortcomings.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
