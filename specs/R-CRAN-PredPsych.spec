%global __brp_check_rpaths %{nil}
%global packname  PredPsych
%global packver   0.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4
Release:          3%{?dist}%{?buildtag}
Summary:          Predictive Approaches in Psychology

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-caret 
BuildRequires:    R-rpart 
BuildRequires:    R-CRAN-e1071 
BuildRequires:    R-CRAN-mclust 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-party 
BuildRequires:    R-CRAN-randomForest 
BuildRequires:    R-CRAN-statmod 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-caret 
Requires:         R-rpart 
Requires:         R-CRAN-e1071 
Requires:         R-CRAN-mclust 
Requires:         R-MASS 
Requires:         R-CRAN-party 
Requires:         R-CRAN-randomForest 
Requires:         R-CRAN-statmod 

%description
Recent years have seen an increased interest in novel methods for
analyzing quantitative data from experimental psychology. Currently,
however, they lack an established and accessible software framework. Many
existing implementations provide no guidelines, consisting of small code
snippets, or sets of packages. In addition, the use of existing packages
often requires advanced programming experience. 'PredPsych' is a
user-friendly toolbox based on machine learning predictive algorithms. It
comprises of multiple functionalities for multivariate analyses of
quantitative behavioral data based on machine learning models.

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
