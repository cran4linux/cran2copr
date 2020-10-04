%global packname  swa
%global packver   0.8.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.8.1
Release:          3%{?dist}%{?buildtag}
Summary:          Subsampling Winner Algorithm for Classification

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.1
Requires:         R-core >= 3.3.1
BuildArch:        noarch
BuildRequires:    R-CRAN-ROCR 
BuildRequires:    R-CRAN-reshape 
BuildRequires:    R-CRAN-ggplot2 
Requires:         R-CRAN-ROCR 
Requires:         R-CRAN-reshape 
Requires:         R-CRAN-ggplot2 

%description
This algorithm conducts variable selection in the classification setting.
It repeatedly subsamples variables and runs linear discriminant analysis
(LDA) on the subsampled variables. Variables are scored based on the AUC
and the t-statistics. Variables then enter a competition and the
semi-finalist variables will be evaluated in a final round of LDA
classification. The algorithm then outputs a list of variable selected.
Qiao, Sun and Fan (2017)
<http://people.math.binghamton.edu/qiao/swa.html>.

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
