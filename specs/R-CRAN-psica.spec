%global __brp_check_rpaths %{nil}
%global packname  psica
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          3%{?dist}%{?buildtag}
Summary:          Decision Tree Analysis for Probabilistic Subgroup Identificationwith Multiple Treatments

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-gridBase 
BuildRequires:    R-CRAN-randomForest 
BuildRequires:    R-rpart 
BuildRequires:    R-CRAN-partykit 
BuildRequires:    R-CRAN-party 
BuildRequires:    R-CRAN-BayesTree 
Requires:         R-CRAN-Rdpack 
Requires:         R-grid 
Requires:         R-CRAN-gridBase 
Requires:         R-CRAN-randomForest 
Requires:         R-rpart 
Requires:         R-CRAN-partykit 
Requires:         R-CRAN-party 
Requires:         R-CRAN-BayesTree 

%description
In the situation when multiple alternative treatments or interventions
available, different population groups may respond differently to
different treatments. This package implements a method that discovers the
population subgroups in which a certain treatment has a better effect than
the other alternative treatments. This is done by first estimating the
treatment effect for a given treatment and its uncertainty by computing
random forests, and the resulting model is summarized by a decision tree
in which the probabilities that the given treatment is best for a given
subgroup is shown in the corresponding terminal node of the tree.

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
%{rlibdir}/%{packname}
