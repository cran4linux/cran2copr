%global packname  translation.ko
%global packver   0.0.1.5.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.1.5.2
Release:          3%{?dist}%{?buildtag}
Summary:          R Manuals Literally Translated in Korean

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.1.5
Requires:         R-core >= 2.1.5
BuildArch:        noarch
BuildRequires:    R-utils 
Requires:         R-utils 

%description
R version 2.1.0 and later support Korean translations of program messages.
The continuous efforts have been made by
<http://developer.r-project.org/TranslationTeams.html> The R Documentation
files are licensed under the General Public License, version 2 or 3.  This
means that the pilot project to translate them into Korean has permission
to reproduce them and translate them.  This work is done with GNU
'gettext' utilities.  The portable object template is updated a weekly
basis or whenever changes are necessary.  Comments and corrections via
email to the maintainer is of course most welcome.  In order to
voluntarily participate in or offer your help with this translation,
please contact the maintainer.  To check the change and progress of Korean
translation, please visit <http://www.openstatistics.net>.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
