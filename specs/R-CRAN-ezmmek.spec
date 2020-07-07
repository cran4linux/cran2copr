%global packname  ezmmek
%global packver   0.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.1
Release:          3%{?dist}
Summary:          Analysis of Enzyme Activities on Synthetic Substrates usingMichaelis-Menten Kinetics

License:          AGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-assertable 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-nls2 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-tidyr 
Requires:         R-CRAN-assertable 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-nls2 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-tidyr 

%description
Analysis of enzyme activities on fluorogenic and chromogenic substrates
using Michaelis-Menten kinetics. It outputs plots and relevant statistics
regarding standard curves and saturation curves. It also enables the user
to customize plots to their particular datasets. This package is based on
concepts described in: German et al. (2011)
<doi:10.1016/j.soilbio.2011.03.017>, Sinsabaugh et al. (2014)
<doi:10.1007/s10533-014-0030-y>, and Steen and Arnosti (2011)
<doi:10.1016/j.marchem.2010.10.006>.

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
%{rlibdir}/%{packname}/INDEX
