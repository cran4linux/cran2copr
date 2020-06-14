%global packname  projections
%global packver   0.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.1
Release:          2%{?dist}
Summary:          Project Future Case Incidence

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-incidence >= 1.4.1
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-distcrete 
BuildRequires:    R-CRAN-ggplot2 
Requires:         R-CRAN-incidence >= 1.4.1
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-distcrete 
Requires:         R-CRAN-ggplot2 

%description
Provides functions and graphics for projecting daily incidence based on
past incidence, and estimates of the serial interval and reproduction
number. Projections are based on a branching process using a
Poisson-distributed number of new cases per day, similar to the model used
for estimating R0 in 'EpiEstim' or in 'earlyR', and described by Nouvellet
et al. (2017) <doi:10.1016/j.epidem.2017.02.012>.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
