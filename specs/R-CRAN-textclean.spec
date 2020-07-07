%global packname  textclean
%global packver   0.9.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.3
Release:          3%{?dist}
Summary:          Text Cleaning Tools

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-mgsub >= 1.5.0
BuildRequires:    R-CRAN-glue >= 1.3.0
BuildRequires:    R-CRAN-english >= 1.0.2
BuildRequires:    R-CRAN-textshape >= 1.0.1
BuildRequires:    R-CRAN-lexicon >= 1.0.0
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-qdapRegex 
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-utils 
Requires:         R-CRAN-mgsub >= 1.5.0
Requires:         R-CRAN-glue >= 1.3.0
Requires:         R-CRAN-english >= 1.0.2
Requires:         R-CRAN-textshape >= 1.0.1
Requires:         R-CRAN-lexicon >= 1.0.0
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-qdapRegex 
Requires:         R-CRAN-stringi 
Requires:         R-utils 

%description
Tools to clean and process text.  Tools are geared at checking for
substrings that are not optimal for analysis and replacing or removing
them (normalizing) with more analysis friendly substrings (see Sproat,
Black, Chen, Kumar, Ostendorf, & Richards (2001)
<doi:10.1006/csla.2001.0169>) or extracting them into new variables. For
example, emoticons are often used in text but not always easily handled by
analysis algorithms.  The replace_emoticon() function replaces emoticons
with word equivalents.

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
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/docs
%{rlibdir}/%{packname}/INDEX
