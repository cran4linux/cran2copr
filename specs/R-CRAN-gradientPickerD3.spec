%global packname  gradientPickerD3
%global packver   0.1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0.0
Release:          2%{?dist}
Summary:          Interactive Color Gradient Picker Using 'htmlwidgets' and theModified JS Script 'jquery-gradient-picker'

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.1
Requires:         R-core >= 3.3.1
BuildArch:        noarch
BuildRequires:    R-CRAN-htmlwidgets 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-shiny 
Requires:         R-CRAN-htmlwidgets 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-shiny 

%description
Widget for an interactive selection and modification of a color gradient.
'gradientPickerD3' allows addition, removement and replacement of color
ticks. List of numeric values will automatically translate in their
corresponding tick position within the numeric range. App returns a
data.frame containing tick values, colors and the positions in percent
(0.0 to 1.0) for each color tick in the gradient. The original JS
'jquery-gradient-picker' was implemented by Matt Crinklaw-Vogt (nick:
tantaman) <https://github.com/tantaman/>. Widget and JS modifications were
done by CD. Peikert.

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
%doc %{rlibdir}/%{packname}/htmlwidgets
%doc %{rlibdir}/%{packname}/snapshots
%{rlibdir}/%{packname}/INDEX
