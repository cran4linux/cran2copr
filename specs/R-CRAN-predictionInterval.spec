%global packname  predictionInterval
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}
Summary:          Prediction Interval Functions for Assessing Replication StudyResults

License:          MIT License + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-MBESS 
BuildRequires:    R-MASS 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-pbapply 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-MBESS 
Requires:         R-MASS 
Requires:         R-stats 
Requires:         R-CRAN-pbapply 

%description
A common problem faced by journal reviewers and authors is the question of
whether the results of a replication study are consistent with the
original published study. One solution to this problem is to examine the
effect size from the original study and generate the range of effect sizes
that could reasonably be obtained (due to random sampling) in a
replication attempt (i.e., calculate a prediction interval). This package
has functions that calculate the prediction interval for the correlation
(i.e., r), standardized mean difference (i.e., d-value), and mean.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
