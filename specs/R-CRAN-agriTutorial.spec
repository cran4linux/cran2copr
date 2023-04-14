%global __brp_check_rpaths %{nil}
%global packname  agriTutorial
%global packver   0.1.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.5
Release:          3%{?dist}%{?buildtag}
Summary:          Tutorial Analysis of Some Agricultural Experiments

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-lmerTest 
BuildRequires:    R-CRAN-emmeans 
BuildRequires:    R-CRAN-pbkrtest 
BuildRequires:    R-lattice 
BuildRequires:    R-nlme 
BuildRequires:    R-CRAN-ggplot2 
Requires:         R-CRAN-lmerTest 
Requires:         R-CRAN-emmeans 
Requires:         R-CRAN-pbkrtest 
Requires:         R-lattice 
Requires:         R-nlme 
Requires:         R-CRAN-ggplot2 

%description
Example software for the analysis of data from designed experiments,
especially agricultural crop experiments. The basics of the analysis of
designed experiments are discussed using real examples from agricultural
field trials. A range of statistical methods using a range of R
statistical packages are exemplified . The experimental data is made
available as separate data sets for each example and the R analysis code
is made available as example code. The example code can be readily
extended, as required.

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
