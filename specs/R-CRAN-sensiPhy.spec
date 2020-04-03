%global packname  sensiPhy
%global packver   0.8.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.8.5
Release:          1%{?dist}
Summary:          Sensitivity Analysis for Comparative Methods

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ape >= 3.3
BuildRequires:    R-CRAN-phylolm >= 2.4
BuildRequires:    R-CRAN-ggplot2 >= 2.1.0
BuildRequires:    R-CRAN-geiger >= 2.0
BuildRequires:    R-CRAN-phytools >= 0.6
BuildRequires:    R-CRAN-caper >= 0.5.2
Requires:         R-CRAN-ape >= 3.3
Requires:         R-CRAN-phylolm >= 2.4
Requires:         R-CRAN-ggplot2 >= 2.1.0
Requires:         R-CRAN-geiger >= 2.0
Requires:         R-CRAN-phytools >= 0.6
Requires:         R-CRAN-caper >= 0.5.2

%description
An implementation of sensitivity analysis for phylogenetic comparative
methods. The package is an umbrella of statistical and graphical methods
that estimate and report different types of uncertainty in PCM: (i)
Species Sampling uncertainty (sample size; influential species and
clades). (ii) Phylogenetic uncertainty (different topologies and/or branch
lengths). (iii) Data uncertainty (intraspecific variation and measurement
error).

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
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
