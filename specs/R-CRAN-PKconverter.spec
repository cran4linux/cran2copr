%global __brp_check_rpaths %{nil}
%global packname  PKconverter
%global packver   1.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.5
Release:          3%{?dist}%{?buildtag}
Summary:          The Parameter Converter of the Pharmacokinetic Models

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-shinythemes 
BuildRequires:    R-CRAN-shinydashboard 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-shinythemes 
Requires:         R-CRAN-shinydashboard 

%description
Pharmacokinetics is the study of drug absorption, distribution,
metabolism, and excretion. The pharmacokinetics model explains that how
the drug concentration change as the drug moves through the different
compartments of the body. For pharmacokinetic modeling and analysis, it is
essential to understand the basic pharmacokinetic parameters. All
parameters are considered, but only some of parameters are used in the
model. Therefore, we need to convert the estimated parameters to the other
parameters after fitting the specific pharmacokinetic model. This package
is developed to help this converting work. For more detailed explanation
of pharmacokinetic parameters, see "Gabrielsson and Weiner" (2007),
"ISBN-10: 9197651001"; "Benet and Zia-Amirhosseini" (1995) <DOI:
10.1177/019262339502300203>; "Mould and Upton" (2012) <DOI:
10.1038/psp.2012.4>; "Mould and Upton" (2013) <DOI: 10.1038/psp.2013.14>.

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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/PKparameter-Formula.pdf
%{rlibdir}/%{packname}/INDEX
