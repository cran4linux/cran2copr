%global packname  QFASA
%global packver   1.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.3
Release:          3%{?dist}
Summary:          Quantitative Fatty Acid Signature Analysis

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2
Requires:         R-core >= 3.2
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-Rsolnp 
BuildRequires:    R-boot 
BuildRequires:    R-CRAN-futile.logger 
BuildRequires:    R-CRAN-gamlss 
BuildRequires:    R-CRAN-gamlss.dist 
Requires:         R-stats 
Requires:         R-CRAN-Rsolnp 
Requires:         R-boot 
Requires:         R-CRAN-futile.logger 
Requires:         R-CRAN-gamlss 
Requires:         R-CRAN-gamlss.dist 

%description
Accurate estimates of the diets of predators are required in many areas of
ecology, but for many species current methods are imprecise, limited to
the last meal, and often biased. The diversity of fatty acids and their
patterns in organisms, coupled with the narrow limitations on their
biosynthesis, properties of digestion in monogastric animals, and the
prevalence of large storage reservoirs of lipid in many predators, led us
to propose the use of quantitative fatty acid signature analysis (QFASA)
to study predator diets.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/exdata
%{rlibdir}/%{packname}/INDEX
