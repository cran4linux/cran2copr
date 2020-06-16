%global packname  pct
%global packver   0.4.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.1
Release:          1%{?dist}
Summary:          Propensity to Cycle Tool

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-stplanr >= 0.2.8
BuildRequires:    R-boot 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-sf 
Requires:         R-CRAN-stplanr >= 0.2.8
Requires:         R-boot 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-sf 

%description
Functions and example data to teach and increase the reproducibility of
the methods and code underlying the Propensity to Cycle Tool (PCT), a
research project and web application hosted at <https://www.pct.bike/>.
For an academic paper on the methods, see Lovelace et al (2017)
<doi:10.5198/jtlu.2016.862>.

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
%doc %{rlibdir}/%{packname}/cycling-potential-to-specific-zones.R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/estimate-cycling-potential-rnet-leeds-simple-example.R
%doc %{rlibdir}/%{packname}/pct_training_solutions.Rmd
%doc %{rlibdir}/%{packname}/pct_training.R
%doc %{rlibdir}/%{packname}/pct-wy.R
%doc %{rlibdir}/%{packname}/rmd
%doc %{rlibdir}/%{packname}/uptake-model.R
%{rlibdir}/%{packname}/INDEX
