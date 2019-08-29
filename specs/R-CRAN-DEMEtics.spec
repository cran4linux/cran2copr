%global packname  DEMEtics
%global packver   0.8-7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.8.7
Release:          1%{?dist}
Summary:          Evaluating the genetic differentiation between populations basedon Gst and D values.

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.8.0
Requires:         R-core >= 2.8.0
BuildArch:        noarch

%description
This package allows to calculate the fixation index Gst (Nei, 1973) and
the differentiation index D (Jost, 2008) pairwise between or averaged over
several populations.  P-values, stating the significance of
differentiation, and 95 percent confidence intervals can be estimated
using bootstrap resamplings. In the case that more than two populations
are compared pairwise, the p-values are adjusted by bonferroni correction
and in several other ways due to the multiple comparison from one data
set.

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
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
