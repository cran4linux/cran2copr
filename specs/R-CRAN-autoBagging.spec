%global __brp_check_rpaths %{nil}
%global packname  autoBagging
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          3%{?dist}%{?buildtag}
Summary:          Learning to Rank Bagging Workflows with Metalearning

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-cluster 
BuildRequires:    R-CRAN-xgboost 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-e1071 
BuildRequires:    R-rpart 
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-CRAN-caret 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-entropy 
BuildRequires:    R-CRAN-lsr 
BuildRequires:    R-CRAN-CORElearn 
BuildRequires:    R-CRAN-infotheo 
BuildRequires:    R-CRAN-minerva 
BuildRequires:    R-CRAN-party 
Requires:         R-cluster 
Requires:         R-CRAN-xgboost 
Requires:         R-methods 
Requires:         R-CRAN-e1071 
Requires:         R-rpart 
Requires:         R-CRAN-abind 
Requires:         R-CRAN-caret 
Requires:         R-MASS 
Requires:         R-CRAN-entropy 
Requires:         R-CRAN-lsr 
Requires:         R-CRAN-CORElearn 
Requires:         R-CRAN-infotheo 
Requires:         R-CRAN-minerva 
Requires:         R-CRAN-party 

%description
A framework for automated machine learning. Concretely, the focus is on
the optimisation of bagging workflows. A bagging workflows is composed by
three phases: (i) generation: which and how many predictive models to
learn; (ii) pruning: after learning a set of models, the worst ones are
cut off from the ensemble; and (iii) integration: how the models are
combined for predicting a new observation. autoBagging optimises these
processes by combining metalearning and a learning to rank approach to
learn from metadata. It automatically ranks 63 bagging workflows by
exploiting past performance and dataset characterization. A complete
description of the method can be found in: Pinto, F., Cerqueira, V.,
Soares, C., Mendes-Moreira, J. (2017): "autoBagging: Learning to Rank
Bagging Workflows with Metalearning" arXiv preprint arXiv:1706.09367.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
