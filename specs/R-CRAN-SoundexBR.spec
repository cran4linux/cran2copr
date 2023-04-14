%global __brp_check_rpaths %{nil}
%global packname  SoundexBR
%global packver   1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2
Release:          3%{?dist}%{?buildtag}
Summary:          Phonetic-Coding for Portuguese

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0
Requires:         R-core >= 3.0
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-graphics 
Requires:         R-grDevices 

%description
The SoundexBR package provides an algorithm for decoding names into
phonetic codes, as pronounced in Portuguese. The goal is for homophones to
be encoded to the same representation so that they can be matched despite
minor differences in spelling. The algorithm mainly encodes consonants; a
vowel will not be encoded unless it is the first letter. The soundex code
resultant consists of a four digits long string composed by one letter
followed by three numerical digits: the letter is the first letter of the
name, and the digits encode the remaining consonants.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
