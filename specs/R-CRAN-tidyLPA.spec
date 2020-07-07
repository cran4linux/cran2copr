%global packname  tidyLPA
%global packver   1.0.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.7
Release:          3%{?dist}
Summary:          Easily Carry Out Latent Profile Analysis (LPA) Using Open-Sourceor Commercial Software

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-gtable 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-mclust 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-mix 
BuildRequires:    R-CRAN-MplusAutomation 
BuildRequires:    R-CRAN-tibble 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-gtable 
Requires:         R-grid 
Requires:         R-CRAN-mclust 
Requires:         R-methods 
Requires:         R-CRAN-mix 
Requires:         R-CRAN-MplusAutomation 
Requires:         R-CRAN-tibble 

%description
An interface to the 'mclust' package to easily carry out latent profile
analysis ("LPA"). Provides functionality to estimate commonly-specified
models. Follows a tidy approach, in that output is in the form of a data
frame that can subsequently be computed on. Also has functions to
interface to the commercial 'MPlus' software via the 'MplusAutomation'
package.

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
