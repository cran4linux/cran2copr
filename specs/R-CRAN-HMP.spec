%global __brp_check_rpaths %{nil}
%global packname  HMP
%global packver   2.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.1
Release:          3%{?dist}%{?buildtag}
Summary:          Hypothesis Testing and Power Calculations for ComparingMetagenomic Samples from HMP

License:          Apache License (== 2.0)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-dirmult 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-vegan 
BuildRequires:    R-CRAN-gplots 
BuildRequires:    R-rpart 
BuildRequires:    R-CRAN-rpart.plot 
BuildRequires:    R-parallel 
BuildRequires:    R-graphics 
BuildRequires:    R-lattice 
Requires:         R-CRAN-dirmult 
Requires:         R-CRAN-ggplot2 
Requires:         R-stats 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-doParallel 
Requires:         R-MASS 
Requires:         R-CRAN-vegan 
Requires:         R-CRAN-gplots 
Requires:         R-rpart 
Requires:         R-CRAN-rpart.plot 
Requires:         R-parallel 
Requires:         R-graphics 
Requires:         R-lattice 

%description
Using Dirichlet-Multinomial distribution to provide several functions for
formal hypothesis testing, power and sample size calculations for human
microbiome experiments.

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
