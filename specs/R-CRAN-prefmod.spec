%global packname  prefmod
%global packver   0.8-34
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.8.34
Release:          3%{?dist}
Summary:          Utilities to Fit Paired Comparison Models for Preferences

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildRequires:    R-CRAN-gnm >= 1.0.0
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-colorspace 
BuildRequires:    R-grDevices 
BuildRequires:    R-utils 
Requires:         R-CRAN-gnm >= 1.0.0
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-CRAN-colorspace 
Requires:         R-grDevices 
Requires:         R-utils 

%description
Generates design matrix for analysing real paired comparisons and derived
paired comparison data (Likert type items/ratings or rankings) using a
loglinear approach. Fits loglinear Bradley-Terry model (LLBT) exploiting
an eliminate feature. Computes pattern models for paired comparisons,
rankings, and ratings. Some treatment of missing values (MCAR and MNAR).
Fits latent class (mixture) models for paired comparison, rating and
ranking patterns using a non-parametric ML approach.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/NEWS.pdf
%doc %{rlibdir}/%{packname}/NEWS.Rd
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
