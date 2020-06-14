%global packname  rdlocrand
%global packver   0.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6
Release:          2%{?dist}
Summary:          Local Randomization Methods for RD Designs

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1
Requires:         R-core >= 3.1
BuildArch:        noarch
BuildRequires:    R-CRAN-AER 
BuildRequires:    R-CRAN-sandwich 
Requires:         R-CRAN-AER 
Requires:         R-CRAN-sandwich 

%description
The regression discontinuity (RD) design is a popular quasi-experimental
design for causal inference and policy evaluation. Under the local
randomization approach, RD designs can be interpreted as randomized
experiments inside a window around the cutoff. This package provides tools
to perform randomization inference for RD designs under local
randomization: rdrandinf() to perform hypothesis testing using
randomization inference, rdwinselect() to select a window around the
cutoff in which randomization is likely to hold, rdsensitivity() to assess
the sensitivity of the results to different window lengths and null
hypotheses and rdrbounds() to construct Rosenbaum bounds for sensitivity
to unobserved confounders. See Cattaneo, Titiunik and Vazquez-Bare (2016)
<https://sites.google.com/site/rdpackages/rdlocrand/Cattaneo-Titiunik-VazquezBare_2016_Stata.pdf>
for further methodological details.

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
