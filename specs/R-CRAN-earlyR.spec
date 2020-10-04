%global packname  earlyR
%global packver   0.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.1
Release:          3%{?dist}%{?buildtag}
Summary:          Estimation of Transmissibility in the Early Stages of a DiseaseOutbreak

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-distcrete 
BuildRequires:    R-CRAN-EpiEstim 
BuildRequires:    R-CRAN-epitrix 
Requires:         R-stats 
Requires:         R-CRAN-distcrete 
Requires:         R-CRAN-EpiEstim 
Requires:         R-CRAN-epitrix 

%description
Implements a simple, likelihood-based estimation of the reproduction
number (R0) using a branching process with a Poisson likelihood. This
model requires knowledge of the serial interval distribution, and dates of
symptom onsets. Infectiousness is determined by weighting R0 by the
probability mass function of the serial interval on the corresponding day.
It is a simplified version of the model introduced by Cori et al. (2013)
<doi:10.1093/aje/kwt133>.

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
