%global packname  baRulho
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          3%{?dist}
Summary:          Quantifying Habitat-Induced Acoustic Signal Degradation

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.1
Requires:         R-core >= 3.2.1
BuildArch:        noarch
BuildRequires:    R-CRAN-warbleR >= 1.1.20
BuildRequires:    R-CRAN-pbapply 
BuildRequires:    R-utils 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-seewave 
BuildRequires:    R-CRAN-tuneR 
Requires:         R-CRAN-warbleR >= 1.1.20
Requires:         R-CRAN-pbapply 
Requires:         R-utils 
Requires:         R-stats 
Requires:         R-CRAN-seewave 
Requires:         R-CRAN-tuneR 

%description
Intended to facilitate acoustic analysis of (animal) sound transmission
experiments, which typically aim to quantify changes in signal structure
when transmitted in a given habitat by broadcasting and re-recording
animal sounds at increasing distances. The package offers a workflow with
functions to prepare the data set for analysis as well as to calculate and
visualize several degradation metrics, including blur ratio,
signal-to-noise ratio, excess attenuation and envelope correlation among
others (Dabelsteen et al 1993 <doi:10.1121/1.406682>).

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
