%global __brp_check_rpaths %{nil}
%global packname  bpcp
%global packver   1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4
Release:          3%{?dist}%{?buildtag}
Summary:          Beta Product Confidence Procedure for Right Censored Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-survival 
BuildRequires:    R-CRAN-ggplot2 
Requires:         R-stats 
Requires:         R-survival 
Requires:         R-CRAN-ggplot2 

%description
Calculates nonparametric pointwise confidence intervals for the survival
distribution for right censored data, and for medians [Fay and Brittain
<doi:10.1002/sim.6905>]. Has two-sample tests for dissimilarity (e.g.,
difference, ratio or odds ratio) in survival at a fixed time, and
differences in medians [Fay, Proschan, and Brittain
<doi:10.1111/biom.12231>]. Especially important for latter parts of the
survival curve, small sample sizes or heavily censored data. Includes
mid-p options.

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
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
