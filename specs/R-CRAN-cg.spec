%global packname  cg
%global packver   1.0-3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.3
Release:          3%{?dist}
Summary:          Compare Groups, Analytically and Graphically

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.3
Requires:         R-core >= 3.2.3
BuildArch:        noarch
BuildRequires:    R-CRAN-Hmisc >= 3.17.1
BuildRequires:    R-CRAN-VGAM >= 1.0.0
BuildRequires:    R-methods 
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-grid 
BuildRequires:    R-MASS 
BuildRequires:    R-lattice 
BuildRequires:    R-survival 
BuildRequires:    R-CRAN-multcomp 
BuildRequires:    R-nlme 
BuildRequires:    R-CRAN-rms 
Requires:         R-CRAN-Hmisc >= 3.17.1
Requires:         R-CRAN-VGAM >= 1.0.0
Requires:         R-methods 
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-grid 
Requires:         R-MASS 
Requires:         R-lattice 
Requires:         R-survival 
Requires:         R-CRAN-multcomp 
Requires:         R-nlme 
Requires:         R-CRAN-rms 

%description
Comprehensive data analysis software, and the name "cg" stands for
"compare groups." Its genesis and evolution are driven by common needs to
compare administrations, conditions, etc. in medicine research and
development. The current version provides comparisons of unpaired samples,
i.e. a linear model with one factor of at least two levels. It also
provides comparisons of two paired samples. Good data graphs, modern
statistical methods, and useful displays of results are emphasized.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/INDEX
