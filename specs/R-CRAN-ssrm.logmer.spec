%global packname  ssrm.logmer
%global packver   0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1
Release:          3%{?dist}
Summary:          Sample Size Determination for Longitudinal Designs with BinaryOutcome

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-statmod 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-sfsmisc 
Requires:         R-CRAN-statmod 
Requires:         R-stats 
Requires:         R-CRAN-sfsmisc 

%description
Provides the necessary sample size for a longitudinal study with binary
outcome in order to attain a pre-specified power while strictly
maintaining the Type I error rate. Kapur K, Bhaumik R, Tang XC, Hur K,
Reda DJ, Bhaumik D (2014) <doi:10.1002/sim.6203>.

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
