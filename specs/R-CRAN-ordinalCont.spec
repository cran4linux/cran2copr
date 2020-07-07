%global packname  ordinalCont
%global packver   2.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.1
Release:          3%{?dist}
Summary:          Ordinal Regression Analysis for Continuous Scales

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-boot 
BuildRequires:    R-splines 
BuildRequires:    R-CRAN-Deriv 
Requires:         R-boot 
Requires:         R-splines 
Requires:         R-CRAN-Deriv 

%description
A regression framework for response variables which are continuous
self-rating scales such as the Visual Analog Scale (VAS) used in pain
assessment, or the Linear Analog Self-Assessment (LASA) scales in quality
of life studies. These scales measure subjects' perception of an
intangible quantity, and cannot be handled as ratio variables because of
their inherent non-linearity. We treat them as ordinal variables, measured
on a continuous scale. A function (the g function) connects the scale with
an underlying continuous latent variable. The link function is the inverse
of the CDF of the assumed underlying distribution of the latent variable.
A variety of link functions are currently implemented.

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
%{rlibdir}/%{packname}/INDEX
