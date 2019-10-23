%global packname  qqtest
%global packver   1.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.1
Release:          1%{?dist}
Summary:          Self Calibrating Quantile-Quantile Plots for Visual Testing

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10.0
Requires:         R-core >= 2.10.0
BuildArch:        noarch
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-robust 
BuildRequires:    R-stats 
Requires:         R-grDevices 
Requires:         R-CRAN-robust 
Requires:         R-stats 

%description
Provides the function qqtest which incorporates uncertainty in its qqplot
display(s) so that the user might have a better sense of the evidence
against the specified distributional hypothesis.  qqtest draws a quantile
quantile plot for visually assessing whether the data come from a test
distribution that has been defined in one of many ways.  The vertical axis
plots the data quantiles, the horizontal those of a test distribution. The
default behaviour generates 1000 samples from the test distribution and
overlays the plot with shaded pointwise interval estimates for the ordered
quantiles from the test distribution.  A small number of independently
generated exemplar quantile plots can also be overlaid.  Both the interval
estimates and the exemplars provide different comparative information to
assess the evidence provided by the qqplot for or against the hypothesis
that the data come from the test distribution (default is normal or
gaussian).  Finally, a visual test of significance (a lineup plot) can
also be displayed to test the null hypothesis that the data come from the
test distribution.

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
