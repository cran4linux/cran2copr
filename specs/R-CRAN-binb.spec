%global __brp_check_rpaths %{nil}
%global packname  binb
%global packver   0.0.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.6
Release:          3%{?dist}%{?buildtag}
Summary:          'binb' is not 'Beamer'

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-rmarkdown 
BuildRequires:    R-CRAN-knitr 
Requires:         R-CRAN-rmarkdown 
Requires:         R-CRAN-knitr 

%description
A collection of 'LaTeX' styles using 'Beamer' customization for pdf-based
presentation slides in 'RMarkdown'. At present it contains 'RMarkdown'
adaptations of the LaTeX themes 'Metropolis' (formerly 'mtheme') theme by
Matthias Vogelgesang and others (now included in 'TeXLive'), the 'IQSS' by
Ista Zahn (which is included here), and the 'Monash' theme by Rob J
Hyndman. Additional (free) fonts may be needed: 'Metropolis' prefers
'Fira', and 'IQSS' requires 'Libertinus'.

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
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/iqssDemo
%doc %{rlibdir}/%{packname}/monashDemo
%doc %{rlibdir}/%{packname}/NEWS.Rd
%doc %{rlibdir}/%{packname}/presentoDemo
%doc %{rlibdir}/%{packname}/rmarkdown
%{rlibdir}/%{packname}/INDEX
