%global debug_package %{nil}
%global packname  ccrs
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          3%{?dist}
Summary:          Correct and Cluster Response Style Biased Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-cds 
BuildRequires:    R-CRAN-colorspace 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-limSolve 
BuildRequires:    R-CRAN-lsbclust 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-msm 
BuildRequires:    R-parallel 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-cds 
Requires:         R-CRAN-colorspace 
Requires:         R-CRAN-dplyr 
Requires:         R-graphics 
Requires:         R-CRAN-limSolve 
Requires:         R-CRAN-lsbclust 
Requires:         R-methods 
Requires:         R-CRAN-msm 
Requires:         R-parallel 
Requires:         R-stats 
Requires:         R-utils 

%description
Functions for performing Correcting and Clustering response-style-biased
preference data (CCRS). The main functions are correct.RS() for correcting
for response styles, and ccrs() for simultaneously correcting and
content-based clustering. The procedure begin with making rank-ordered
boundary data from the given preference matrix using a function called
create.ccrsdata(). Then in correct.RS(), the response style is corrected
as follows: the rank-ordered boundary data are smoothed by I-spline
functions, the given preference data are transformed by the smoothed
functions. The resulting data matrix, which is considered as
bias-corrected data, can be used for any data analysis methods. If one
wants to cluster respondents based on their indicated preferences
(content-based clustering), ccrs() can be applied to the given
(response-style-biased) preference data, which simultaneously corrects for
response styles and clusters respondents based on the contents. Also, the
correction result can be checked by plot.crs() function.

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
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
