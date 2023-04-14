%global __brp_check_rpaths %{nil}
%global packname  flacco
%global packver   1.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.8
Release:          3%{?dist}%{?buildtag}
Summary:          Feature-Based Landscape Analysis of Continuous and ConstrainedOptimization Problems

License:          BSD_2_clause + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-BBmisc 
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-mlr 
Requires:         R-CRAN-BBmisc 
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-mlr 

%description
Tools and features for "Exploratory Landscape Analysis (ELA)" of
single-objective continuous optimization problems. Those features are able
to quantify rather complex properties, such as the global structure,
separability, etc., of the optimization problems.

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
