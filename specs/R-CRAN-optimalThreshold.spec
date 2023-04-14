%global __brp_check_rpaths %{nil}
%global packname  optimalThreshold
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          3%{?dist}%{?buildtag}
Summary:          Bayesian Methods for Optimal Threshold Estimation

License:          GPL (>= 2.0)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.2
Requires:         R-core >= 3.1.2
BuildArch:        noarch
BuildRequires:    R-CRAN-ars 
BuildRequires:    R-CRAN-rjags 
BuildRequires:    R-CRAN-HDInterval 
BuildRequires:    R-mgcv 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-grDevices 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
Requires:         R-CRAN-ars 
Requires:         R-CRAN-rjags 
Requires:         R-CRAN-HDInterval 
Requires:         R-mgcv 
Requires:         R-utils 
Requires:         R-CRAN-coda 
Requires:         R-grDevices 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-graphics 

%description
Functions to estimate the optimal threshold of diagnostic markers or
treatment selection markers. The optimal threshold is the marker value
that maximizes the utility of the marker based-strategy (for diagnostic or
treatment selection) in a given population. The utility function depends
on the type of marker (diagnostic or treatment selection), but always
takes into account the preferences of the patients or the physician in the
decision process. For estimating the optimal threshold, ones must specify
the distributions of the marker in different groups (defined according to
the type of marker, diagnostic or treatment selection) and provides data
to estimate the parameters of these distributions. Ones must also provide
some features of the target populations (disease prevalence or treatment
efficacies) as well as the preferences of patients or physicians. The
functions rely on Bayesian inference which helps producing several
indicators derived from the optimal threshold. See Blangero, Y, Rabilloud,
M, Ecochard, R, and Subtil, F (2019) <doi:10.1177/0962280218821394> for
the original article that describes the estimation method for treatment
selection markers and Subtil, F, and Rabilloud, M (2019)
<doi:10.1002/bimj.200900242> for diagnostic markers.

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
